from typing import Dict, Optional



class IsNoProfit():
    name = 'is_no_profit'
    depends_on = []

    def extract_one(self, snapshot: Dict, features: Dict[str, Dict]) -> Optional[Dict]:
        description = snapshot.get('description')

	name = snapshot.get('name')

        if description is None:
            return None

        entity_tokens = ['we are a ', 'we are an independent ',
                         f'{name} is ', f'{name} is a ', f'{name} is an independent ']
        no_profit_tokens = [
            'not for profit',
            'not-for-profit',
            'not for-profit',
            'not-for profit',
            'no profit',
            'no-profit',
            'not-profit',
            'not profit',
            'nonprofit',
            'non-profit',
            'non profit',
        ]

        for entity in entity_tokens:
            for profit in no_profit_tokens:
                string = entity + profit
                if string in combined_description:
                    return {'score':1)

        return {'score': 0}

