import json

import requests


class FiroWalletAPI:

    def __init__(self, httpprovider):
        self.httpprovider = httpprovider

    """
        Create new wallet for new bot member
    """

    def create_user_wallet(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {"jsonrpc": "1.0", "id": 1, "method": "getsparkdefaultaddress"}
            )).json()
        print(response)
        return response['result']

    """
        Fetch list of txs
    """

    def get_txs_list(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {"jsonrpc": "1.0", "id": 2, "method": "listtransactions", "params": ["*", 100]}
            )).json()

        return response

    def listsparkmints(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {"jsonrpc": "1.0", "id": 2, "method": "listsparkmints"}
            )).json()
        print(response)
        return response

    # TODO - REMOVE
    def listlelantusmints(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {"jsonrpc": "1.0", "id": 2, "method": "listlelantusmints"}
            )).json()

        return response

    """
        Get wallet status
    """

    def get_wallet_status(self):
        try:
            response = requests.post(
                self.httpprovider,
                data=json.dumps(
                    {
                        "jsonrpc": "1.0",
                        "id": 6,
                        "method": "getinfo",
                    })).json()

            print(response)
            return response
        except Exception as exc:
            print(exc)

    """
        Get transaction status
    """

    def get_tx_status(self, tx_id):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "gettransaction",
                    "params":
                        {
                            "txid": "%s" % tx_id
                        }
                })).json()

        print(response)
        return response

    """ 
    """

    def automintunspent(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "automintspark",
                })).json()

        print(response)
        return response

    """
            Sends privately if to a Spark address, or deshields if to a transparent address.
        """

    def spendspark(self, address, value, memo=""):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "spendspark",
                    "params": [
                        {
                            address: {"amount": value, "memo": memo, "subtractFee": False}
                        }
                    ]

                })).json()
        return response

    """
        Anonymizes (mints) transparent balance to a Spark address
    """

    def mintspark(self, address, value):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "mintspark",
                    "params": [
                        {
                            address: {"amount": value, "memo": "", "subtractFee": False}
                        }
                    ]

                })).json()
        return response

    """
        Send Transaction 
    """

    # def joinsplit(self, address, value):
    #     response = requests.post(
    #         self.httpprovider,
    #         data=json.dumps(
    #             {
    #                 "jsonrpc": "1.0",
    #                 "id": 4,
    #                 "method": "joinsplit",
    #                 "params": [{address: value}]
    #             })).json()
    #
    #     print(response)
    #     return response

    """ 
    """

    def listsparkspends(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "listsparkspends",
                })).json()
        print(response)
        return response
    # def listlelantusjoinsplits(self):
    #     response = requests.post(
    #         self.httpprovider,
    #         data=json.dumps(
    #             {
    #                 "jsonrpc": "1.0",
    #                 "id": 4,
    #                 "method": "listlelantusjoinsplits",
    #                 "params": [100]
    #             })).json()
    #     print(response)
    #     return response

    """
    """

    def lelantustospark(self):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 4,
                    "method": "lelantustospark",
                })).json()
        print(response)
        return response

    """
        Validate address
    """

    def validate_address(self, address):
        response = requests.post(
            self.httpprovider,
            data=json.dumps(
                {
                    "jsonrpc": "1.0",
                    "id": 1,
                    "method": "validateaddress",
                    "params":
                        {
                            "address": address
                        }
                })).json()
        return response
