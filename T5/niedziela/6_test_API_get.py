from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #utwórz kontekst API - inny niz przeglądarki
    request_context = p.request.new_context()
    #wysyłamy zadanie GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    #sprawdzamy status odpowiedzi
    status = response.status

    print(f"Status odpowiedzi: {status}")
    assert status == 200

    body = response.json()
    print(body)

    id = body["id"] #spodziewamy się 1
    userid = body["userId"] #spodziewamy się 1
    title = body["title"]
    body = body["body"]

    print(f"Id to {id}.")
    print(f"UserId to {userid}.")
    print(f"Title to {title}.")
    print(f"Body to {body}.")

    assert id == 1
    assert userid == 1

    print(f"Typ title to string: ", isinstance(title,str))
    assert isinstance(title, str)