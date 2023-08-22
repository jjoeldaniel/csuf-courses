class CourseNotFound(Exception):
    pass


class Course:
    def __init__(self, json: dict):
        if "error" in json.keys():
            raise CourseNotFound(json["error"])

        self.title = json["title"]
        self.description = json["description"]
        self.prerequisites = json["prerequisites"]
        self.corequisites = json["corequisites"]
