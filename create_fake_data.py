from faker import Faker
import pandas as pd
def create_data(n):
    fake = Faker()
    data = [fake.profile() for i in range(n)]
    data = pd.DataFrame(data)
    data.to_csv(r"data.csv")

if __name__=="__main__":
    n = 50
    create_data(n)

