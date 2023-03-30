from frontend.clock import Clock


def main():
    cl = Clock()

    if cl.delta > 54000:
        print('Stop! More than 15h on...')
        cl.startPause()
        cl.stop()


if __name__ == "__main__":
    main()
