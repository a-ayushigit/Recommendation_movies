
def main():
    from faker import Faker 
    fake = Faker('en_IN')
    for _ in range(10):
        print(fake.street_address())

if __name__ == '__main__':
    main()