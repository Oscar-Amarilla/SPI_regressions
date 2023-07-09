import matplotlib.pyplot as plt

def mei_vs_spi(mei_ts,spi_ts,key):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5),layout='constrained', gridspec_kw={'width_ratios': [5, 2]})

    ax1.plot(spi_ts)
    ax1.plot(mei_ts)
    ax1.axhline(y=-1, color='black', linestyle='--')
    ax1.axhline(y=1, color='black', linestyle='--')
    ax1.set_xlabel('Años')
    ax1.set_ylabel('SPI 2/MEI')
    years = range(1981, 2012)
    tick_positions = [(year-1981)*12 for year in years]
    ax1.set_xticks(tick_positions, years);

    ax2.scatter(spi_ts, mei_ts)
    ax2.plot(spi_ts,spi_ts,color='green')
    ax2.set_xlabel('SPI 2')
    ax2.set_ylabel('MEI')

    fig.suptitle('Estación - '+ key, fontsize=16);
