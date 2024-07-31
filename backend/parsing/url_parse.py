def get_url(display_recipient, title, stream_id):
    syms = ["_", "-", ".", "~"]
    for el in display_recipient:
        if not el.isalpha() and el not in syms and not el.isdigit():
            display_recipient = display_recipient.replace(el, "." + hex(ord(el))[2:].upper())
    display_recipient = display_recipient.replace(".20", "-")
    for el in title:
        if not el.isalpha() and el not in syms and not el.isdigit():
            title = title.replace(el, "." + hex(ord(el))[2:].upper())
    url = f"https://chat.fhir.org/#narrow/stream/{stream_id}-{display_recipient}/topic/{title}"
    return url
