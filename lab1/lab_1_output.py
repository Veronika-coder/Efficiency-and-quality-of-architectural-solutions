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

    def prepare_thread(self):
        print("Preparing thread...")

    def thread_needle(self):
        print("Threading needle...")

    def stitch_pattern(self):
        print("Stitching pattern...")

    def trim_thread(self):
        print("Trimming thread...")

pattern = "flower"
embroidery = Embroidery(pattern)
embroidery.stitch()
