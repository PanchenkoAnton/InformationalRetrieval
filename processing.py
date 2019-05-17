from model_processing import NewDocument


def parse_files(filename, counter):
    with open(filename, errors='ignore') as file:
        text = ''
        for line in file:
            text = text + line
        document = NewDocument(file_name=counter, title=f'Document #{counter}', text=text)
        document.save()


def search(query_type, query_text):
    counter = 0
    for instance in NewDocument.search().query(query_type, text=query_text).execute():
        i = instance.text.lower().find(query_text.lower())
        if i == -1:
            print(f'{instance.title} {instance.text[:20]}')
            counter += 1
            continue
        print(f'{instance.title} {instance.text[i:i+20]}')
        counter += 1
    print(counter)
