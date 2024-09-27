# Understand How EBS Snapshots Work
## Incremental Snapshots
### Let/s say there is an EBS volume with size 8 GB. It is occupied 4 GB and rest 4 GB is free. When I take snapshot of this volume, the snapshot shows size as 8 GB. How is the snapshot incremental then?

#### Why the Snapshot Size Shows as 8GB:

    Incremental Snapshots: EBS snapshots only capture the changed data blocks since the last snapshot. In your case, with only 4GB used, the incremental change would indeed be much smaller.
    Displayed Size: However, the AWS console shows the total size the snapshot represents, which is the full 8GB of your EBS volume. This signifies the potential data it can restore at that point in time.

#### What You're Actually Billed For:

    Storage Cost: You are only billed for the actual storage used by the incremental changes in the snapshot. In your scenario, this would be significantly less than 8GB (likely closer to 4GB).

#### Understanding the Discrepancy:

#### Think of it like a compressed archive:

    The full EBS volume (8GB) is like the original uncompressed files.
    The incremental snapshot is like a compressed archive containing only the changed files (smaller size).
    However, to restore the data from the snapshot, you'd need the full 8GB, just like you'd need to extract the original files from the archive.

#### Here are some additional points:

    There's no way to directly view the actual size of the incremental data within the snapshot in the AWS console.
    Deleting a single snapshot might not free up space immediately if other snapshots reference the same data blocks.

#### Recommendations:

    Don't be alarmed by the displayed snapshot size. It's the full volume representation, not the actual storage used.
    Focus on the billing aspect. You'll only be charged for the incremental data stored in the snapshot.
    Consider using tools like AWS Cost Explorer to track your EBS snapshot storage costs more precisely.


## Deleting Snapshots
### So what happens when one of the incremental snapshot is deleted? do I completely loose that part of data?

Deleting an incremental snapshot doesn't necessarily mean you'll lose data.

Here's how it works:

    Data Retention: If the data in that deleted snapshot is referenced by other, later snapshots, it won't be deleted. This is because AWS doesn't want to risk losing data that might be needed for restoration.   

    Data Deletion: However, if the deleted snapshot contains data that is unique to it (not referenced by any other snapshot), then that data will be deleted. This is to free up storage space.

To summarize:

    If you delete an old snapshot:
        Data referenced by later snapshots will be retained.
        Unique data will be deleted.
    If you delete a recent snapshot:
        There's a higher chance of data being deleted, especially if you haven't taken any snapshots since then.

Therefore, it's generally recommended to keep at least one or two recent snapshots to protect against accidental data loss. You can use AWS's built-in retention policies to automate this process.

### Please refer [AWS Documentation](https://docs.aws.amazon.com/ebs/latest/userguide/how_snapshots_work.html) for more information
