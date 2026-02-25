import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('TasksAndLevels')

def seed_150_tasks():
    print("Rozpoczynam zasilanie bazy 150 zadaniami...")
    
    with table.batch_writer() as batch:
        for i in range(1, 151):
            required_lvl = (i // 15) + 1
            
            task_item = {
                'userId': f'task_{i}', 
                'task_number': i,
                'title': f'Zadanie Chmurowe nr {i}',
                'required_level': required_lvl,
                'status': 'active'
            }
            
            batch.put_item(Item=task_item)
            
            if i % 25 == 0:
                print(f"Zapisano {i}/150 zadań...")
                
    print("Zakończono sukcesem!")

if __name__ == '__main__':
    seed_150_tasks()