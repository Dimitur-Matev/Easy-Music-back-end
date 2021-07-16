from svc import Service

def main():
    Service()

    import models
    import endpoints
    
    Service().run()

if __name__ == "__main__":
    main()

