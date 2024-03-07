import unittest
from dotenv import dotenv_values
from pathlib import Path
import sys
import json
import time

# Add the root directory of your project to the Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from fd_zenmoney.services.zenmoney_service import ZenmoneyService
from fd_zenmoney.schemas import Instrument, Account, Transaction, Country, Company, User, Tag, Budget, Merchant, Reminder, ReminderMarker, DiffObject

settings = dotenv_values(f"{root_dir}/.env")


class TestZenmoneyService(unittest.TestCase):

    def setUp(self) -> None:
        self.Zen = ZenmoneyService(settings.get("ZEN_MONEY_TOKEN"))
        with open("zenmoney_diff.json", "r") as file:
            self.diff_data = json.load(file)
        return super().setUp()
    

    def tearDown(self) -> None:
        return super().tearDown()
    

    def test_fetch_zenmoney_diff_from_api(self):
        diff_object = DiffObject(
            currentClientTimestamp=int(time.time()),
            serverTimestamp=0
        )
        data = self.Zen.sync_zenmoney_diff(diff_object)
        # data = self.diff_data
        self.assertIsNotNone(data)
        self.assertIsInstance(data, DiffObject)
        # for key in data.model_dump().keys():
        #     self.assertIn(key, ["currentClientTimestamp", "serverTimestamp", "forceFetch", "instrument", "country", "company", "user", "account", "tag", "budget", "merchant", "reminder", "reminderMarker", "transaction", "deletion"])


    def test_instruments(self):
        instruments = [Instrument(**d) for d in self.diff_data.get("instrument")]
        self.assertTrue(all(isinstance(item, Instrument) for item in instruments))


    def test_accounts(self):
        accounts = [Account(**d) for d in self.diff_data.get("account")]
        self.assertTrue(all(isinstance(item, Account) for item in accounts))
        # for account in accounts:
        #     print(f"{account.id} => {account.title}: {account.balance}")

        
    def test_transactions(self):
        transactions = [Transaction(**d) for d in self.diff_data.get("transaction")]
        self.assertTrue(all(isinstance(item, Transaction) for item in transactions))
        # print(transactions)


    def test_countries(self):
        countries = [Country(**d) for d in self.diff_data.get("country")]
        self.assertTrue(all(isinstance(item, Country) for item in countries))
        print(f"CONTRIES: {len(countries)}")
    
    
    def test_companies(self):
        companies = [Company(**d) for d in self.diff_data.get("company")]
        self.assertTrue(all(isinstance(item, Company) for item in companies))
        print(f"COMPANIES: {len(companies)}")
    
    
    def test_users(self):
        users = [User(**d) for d in self.diff_data.get("user")]
        self.assertTrue(all(isinstance(item, User) for item in users))
        print(f"USERS: {len(users)}")
    
    
    def test_tags(self):
        tags = [Tag(**d) for d in self.diff_data.get("tag")]
        self.assertTrue(all(isinstance(item, Tag) for item in tags))
        print(f"TAGS: {len(tags)}")


    def test_budgets(self):
        budgets = [Budget(**d) for d in self.diff_data.get("budget")]
        self.assertTrue(all(isinstance(item, Budget) for item in budgets))
        print(f"BUDGETS: {len(budgets)}")


    def test_merchants(self):
        merchants = [Merchant(**d) for d in self.diff_data.get("merchant")]
        self.assertTrue(all(isinstance(item, Merchant) for item in merchants))
        print(f"MERCHANTS: {len(merchants)}")


    def test_reminders(self):
        reminders = [Reminder(**d) for d in self.diff_data.get("reminder")]
        self.assertTrue(all(isinstance(item, Reminder) for item in reminders))
        print(f"REMINDERS: {len(reminders)}")


    def test_reminder_markers(self):
        markers = [ReminderMarker(**d) for d in self.diff_data.get("reminderMarker")]
        self.assertTrue(all(isinstance(item, ReminderMarker) for item in markers))
        print(f"REMINDER MARKERS: {len(markers)}")


if __name__ == '__main__':
    unittest.main()