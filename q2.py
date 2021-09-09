# Martin Vickgren

# import sys


def parseMessage(inputString):
    tmpPos = 4
    length = len(inputString)
    tmp = inputString[tmpPos:length:1]          # Returns a string equivalent of inputString from index tmpPos and
                                                # forward, we do this to remove "GET " and store the rest in tmp.
                                                # 1 is the step, 1 means every character in the range, 2 would mean
                                                # every second character in the range etc

    tmpPos = tmp.find(" ")                      # At the end of the address there will be a space
    requestedResource = tmp[0:tmpPos:1]         # Since the start of tmp is now the start of the address we copy from
                                                # the start of tmp to tmpPos and now the address is stored

    tmp = tmp[tmpPos + 1:length:1]              # tmpPos + 1 to locate the start of HTTP version
    tmpPos = tmp.find("\r")                     # The end of HTTP version is "\r" so we update tmpPos
    httpVersion = tmp[0:tmpPos:1]               # We store the HTTP version

    tmpPos = tmp.find("User-Agent: ")           # In front of the browser we will have "User-Agent: "
    length = len(tmp)
    tmp = tmp[tmpPos + 12:length:1]             # From the end of "User-Agent: " and in front we remove out of tmp
    tmpPos = tmp.find("\r")                     # End of client browser is "\r"
    clientBrowser = tmp[0:tmpPos:1]             # We store the client browser

    tmpPos = tmp.find("Accept-Language: ")      # In front of the language we will have "Accept-Language: "
    tmp = tmp[tmpPos + 17:length:1]             # From the end of "Accept-Language: " and in front we remove out of tmp
    tmpPos = tmp.find("\r")                     # End of language is "\r"
    language = tmp[0:tmpPos:1]                  # We store the language

    return requestedResource, clientBrowser, httpVersion, language


def main():
    string1 = 'GET /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n'

    functionOutput = parseMessage(string1)
    print(functionOutput)
    # Here you will print:
    # the requested_resource,
    # the client’s_browser
    # the HTTP version
    # the language


main()
