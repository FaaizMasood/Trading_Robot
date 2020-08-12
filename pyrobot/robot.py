import pandas as pd
from td.client import TDClient
from td.utils import milliseconds_since_epoch
from datetime import datetime
from datetime import time
from datetime import timezone
from typing import List
from typing import Dict 
from typing import Union
# this is our main object .......hiiiiii
class PyRobot():
# special method , will run every time we 
# create a new instance of this object
# always need client ID , Need URL , Need creditials path , need a trading account to where we 
# are going to place trades 
    def__init__(self, client_id : str, redirect_url: str, credentials_path: str = None, trading_account:str = None,) -> None:
    """[summary]

    Args:
        client_id (str): [description]
        redirect_url (str): [description]
        credentials_path (str, optional): [description]. Defaults to None.
        trading_account (str, optional): [description]. Defaults to None.
    """
        self.trading_account : str = trading_account
        self.client_id : str = client_id
        self.redirect_url: str = redirect_url
        self.credentials_path : str = credentials_path
        # a private method which we will create below
        # session property will represent TD client object and it will be returned from 
        # the _create_session() method ("_" beofre represents private method)
        self.session: TDClient = self._create_session()
        self.trades: dict = ()
        self.historical_prices : dict = ()
        self.stock_frame = None

# here we are defining our _create session method
    def _create_session(self) -> TDClient:
        """[summary]

        Returns:
            TDClient: [description]
        """
        # TD client instance  
        td_client = TDClient(
            client_id = self.client_id,
            redirect_uri = self.redirect_uri,
            credentials_path= self.credentials_path
        )

        # now we need lo log in 
        td_client.login()
        return td_client

    
# we have to see if market is open or not 
# right now it will fail because it doesnot work on weekends
    @property
    def pre_market_open(self) -> bool:
        pre_market_start_time = datetime.now().replace(hour=12,minute=00,second=00,tzinfo=timezone.utc)
        market_start_time = datetime.now().replace(hour=13,minute=30,second=00,tzinfo=timezone.utc).timestamp
        right_now = datetime.now().replace(timezone.utc).timestamp()
        #check if pre market is open or not 
        if(market_start_time >= right_now >= pre_market_start_time):
            return True
        else:
            return False
    @property
    def pot_market_open(self) -> bool:
        post_market_end_time = datetime.now().replace(hour=22,minute=30,second=00,tzinfo=timezone.utc)
        market_end_time = datetime.now().replace(hour=20,minute=00,second=00,tzinfo=timezone.utc).timestamp
        right_now = datetime.now().replace(timezone.utc).timestamp()
        #check if pre market is open or not 
        if(post_market_end_time >= right_now >= market_end_time):
            return True
        else:
            return False
    @property
    def regular_market_open(self) -> bool:
        market_start_time = datetime.now().replace(hour=13,minute=30,second=00,tzinfo=timezone.utc)
        market_end_time = datetime.now().replace(hour=20,minute=00,second=00,tzinfo=timezone.utc).timestamp
        right_now = datetime.now().replace(timezone.utc).timestamp()
        #check if pre market is open or not 
        if(market_end_time >= right_now >= market_start_time):
            return True
        else:
            return False

    # potfolio object
    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List(Dict):
        pass

    def create_stoc_frame(self):
        pass

