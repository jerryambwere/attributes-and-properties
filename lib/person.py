#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name,job="Admin") -> None:
        self.name=name
        self.job=job

    def get_job(self):
        return self._job
    
    def set_job(self,value):
        if value in Person.approved_jobs:
            self._job=value
        else:
            print("Job must be in list of approved jobs.")

        pass
    pass
