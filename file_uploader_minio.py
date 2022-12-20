from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server, its access key
    # and secret key.
    client = Minio(
        "172.17.0.2:9000",
        access_key="accesskey",
        secret_key="secretkey",
        secure=False
    )

    # Make 'landing' bucket if not exist.
    found = client.bucket_exists("landing")
    if not found:
        client.make_bucket("landing")
    else:
        print("Bucket 'landing' already exists")

    # Upload '2010-summary.json' as object name
    # 'summary2010.json' to bucket 'landing'.
    client.fput_object(
        "landing", "summary2010.json", "landing/2010-summary.json",
    )
    print(
        "'2010-summary.json' is successfully uploaded as "
        "object 'summary2010.json' to bucket 'landing'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
