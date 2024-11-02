#!/usr/bin/env python3
"""simple_pagination module"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters."""
    return ((page - 1) * page_size, page * page_size)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the correct page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        si, ei = index_range(page, page_size)
        dataset = self.dataset()
        if si >= len(dataset):
            return []
        return dataset[si:ei]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get a page from the dataset with hypermedia metadata.
        Args: page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
        Returns: Dict: A dictionary containing the page data and
        hypermedia metadata. """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
