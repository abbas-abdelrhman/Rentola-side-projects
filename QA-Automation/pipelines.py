from scrapy.pipelines.files import FilesPipeline


class DownfilesPipeline():

    def file_path(self, request, response=None, info=None):
        file_name: str = request.url.split("/")[-1]
        return file_name
