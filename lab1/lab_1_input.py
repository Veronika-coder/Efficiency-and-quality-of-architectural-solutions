class Embroidery:
    def __init__(self, pattern):
        self.pattern = pattern

    def stitch(self):
        print("Starting embroidery process...")
        self.prepare_thread()
        self.thread_needle()
        self.stitch_pattern()
        self.trim_thread()
        print("Embroidery finished!")
        print("Preparing thread...")
        print("Threading needle...")
        print("Stitching pattern...")
        print("Trimming thread...")

pattern = "flower"
embroidery = Embroidery(pattern)
embroidery.stitch()
