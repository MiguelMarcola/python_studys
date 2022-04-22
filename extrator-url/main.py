class UrlExtrator:
    def __init__(self, url):
        self.url = url
        self.url_validation()
        self.base_url = self.get_base_url()

    def url_validation(self):
        if(not self.url):
            raise ValueError("Empty Url!")
        else:
            self.clean_url()

    def clean_url(self):
        self.url = self.url.replace(" ", "")
        if(not self.url):
            raise ValueError("Empty Url!")

    def get_base_url(self):
        if(self.url.find("?") != -1):
            url_split = self.url.split("?")
            return url_split[0]
        else:
            return self.url

    def get_params(self):
        if(self.url.find("?") != -1):
            url_split = self.url.split("?")

            if(self.url.find("&") != -1):
                url_split = url_split[1].split("&")
                return url_split
            else:
                return [url_split[1]]
        else:
            raise ValueError("No Params Url!")

    def get_value(self, params):
        response = []
        for param in params:
            response.append(param.split("="))
        return response


url = UrlExtrator("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real")

try:
    params = url.get_params()
    valores = url.get_value(params)

    print(url.base_url)
    print(params)
    print(valores)
except:
    print(url.base_url)
    print("Url sem parâmetros")
