def ft_tqdm(lst: range) -> None:
    """
    A simplified tqdm-like progress bar implementation
    Uses print with carriage return to create a progress bar effect.
    """
    total = len(lst)
    bar_length = 60

    for i, item in enumerate(lst, 1):
        progress = i / total
        filled_length = int(bar_length * progress)

        bar = '█' * filled_length
        bar = bar + ' ' * (bar_length - len(bar))

        percentage = f"{int(progress * 100):3d}"

        output = f"\r{percentage}%|{bar}| {i}/{total}"

        print(output, end='', flush=True)

        yield item

    print()

if __name__ == "__main__":
    pass
