import producer_server


def run_kafka_server():
    """Run Kafka server"""
    # TODO get the json file path
    input_file = "./police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police.department.calls",
        bootstrap_servers="localhost:9093",
        client_id="consumer-no-1"
    )

    return producer


def feed():
    """Create producer and generate data"""
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
