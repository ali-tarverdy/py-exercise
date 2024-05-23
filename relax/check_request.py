import requests
from multiprocessing import Process, Semaphore


THREAD = 15  # TODO : In Same Time Only 15 Process Can Send Request Not More For Prevent From banned



class Downloader(Process):
    def __init__(self, url, filename, lock: Semaphore, *args, **kwargs):
        self._url = url
        self._filename = filename
        self._lock = lock
        self._total = 0
        super().__init__(*args, **kwargs)  # TODO : Perfect Pass

    def run(self):
        try:
            # TODO : User Agent For Some Site That Need To can Access
            user_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                                        " (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

            with self._lock:  # TODO : For Acquire Lock With Context Manager
                res = requests.get(self._url, stream=True, headers=user_agent)
                # TODO : Process Stream in 4192 Byte That Can Store it in Ram
                if res.status_code == 200:
                    with open(self._filename, 'wb') as f:  # TODO : Write Binary Mode
                        for item in res.iter_content(4192):
                            self._total += len(item)  # TODO : For Calculate Total Size Of Any Request
                            f.write(item)
                    print(f"Download From {self._url} complete")
                    # print(f"\rTotal Size of requests is: {self._total}")
                else:
                    print(f"Failed to download from {self._url}.")
                    print(f"Status Code: {res.status_code}")

        except Exception as e:  # TODO : If Any Error Happened
            print(f"Error Downloading from {self._url}: {e} !")

        finally:  # TODO : # Release the semaphore regardless of whether the download was successful or not
            self._lock.release()  # TODO : Release the Process in any Situation Even Error Happened for Prevent deadened


semaphore = Semaphore(THREAD)

thread_storage = []

for t in range(THREAD):  # TODO : For Iterate in Any Process Count
    downloader = Downloader("https://anisa.co.ir", "url.txt", semaphore)
    downloader.start()  # TODO : Start One By One Process
    thread_storage.append(downloader)  # TODO : For Store all  Process To Can Use Later

# TODO : Wait To All Process Finish Their Work
for i in thread_storage:  # TODO : For iterate in Any Process We Save it
    i.join()  # TODO : Wait To End All of Process Then Finish Main Process

# print("All Process Finished")
