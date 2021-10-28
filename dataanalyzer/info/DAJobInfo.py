# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.
from typing import List

from dataanalyzer.info.JobInfo import JobInfo


# class : DAJobInfo
class DAJobInfo(JobInfo):
    def __init__(self, filename: str):
        JobInfo.__init__(self, filename)

        self.job_id = self.job_info_dict.get("job_id")
        self.dataset_format = self.job_info_dict.get("dataset_format")
        self.file_path = self.job_info_dict.get("format_json").get("file_path")

    def get_filepath(self) -> str:
        return self.file_path

    def get_dataset_format(self) -> str:
        return self.dataset_format

    def get_filename(self) -> str:
        return self.job_info_dict.get("format_json").get("file_name")

    def get_field_list(self) -> List:
        return self.job_info_dict.get("format_json").get("field_list")

    def get_instances(self):
        return int(self.job_info_dict.get("n_rows"))

    def __str__(self) -> str:
        return "DataAnalyzerJobInfo = {}".format(self.job_info_dict)
