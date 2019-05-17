import os
import time

from elasticsearch_dsl.connections import connections

from processing import parse_files, search


if __name__ == "main":
    connections.create_connection(hosts=['localhost'])

    path = 'C:\\Users\\panch\\PycharmProjects\\InformationalRetrieval_1\\20news-bydate\\20news-bydate-train'
    counter = 0
    start_time = time.time()
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            tmp_path = os.path.join(dirpath, file)
            parse_files(tmp_path, int(file))
            if counter % 100 == 0:
                print(f'{tmp_path} {file}. {counter} files were processed')
            counter += 1
    elapsed = time.time() - start_time
    print(f'It took {elapsed} seconds to finish processing')

    query_text = 'Hello'
    search('match', query_text)
