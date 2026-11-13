# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 250 windows, 6554 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 649 | 55.9 | 52.3 | $+177.93 | +2.7% | $1177.93 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 522 | 53.4 | 52.1 | $-87.36 | -1.7% | $912.64 | -0.4 | done | can't tell from luck |
| value_ev20 | 116 | 33.6 | 36.7 | $-140.27 | -12.1% | $859.73 | -1.0 | Sun 11:00 AM | too few trades (116/200) |
| value_ev10 | 314 | 36.6 | 40.8 | $-433.26 | -13.8% | $566.74 | -2.1 | done | losing for real |
| trend_filter | 343 | 46.1 | 50.5 | $-439.72 | -12.8% | $560.28 | -2.4 | done | losing for real |
| value_ev5 | 463 | 38.9 | 42.5 | $-585.11 | -12.6% | $414.89 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 522 | 46.6 | 49.9 | $-602.83 | -11.5% | $397.17 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 992 | 50.1 | 51.6 | $-710.54 | -7.2% | $289.46 | -2.4 | done | losing for real |
| coinflip | 992 | 49.3 | 50.9 | $-767.88 | -7.7% | $232.12 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 649 | 44.1 | 49.8 | $-1013.26 | -15.6% | $-13.26 | -4.1 | done | losing for real |
| always_up | 992 | 46.8 | 50.5 | $-1175.06 | -11.8% | $-175.06 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1468 | 46.5 | 49.8 | $-1573.80 |
| ETH | 1635 | 46.7 | 49.1 | $-1726.02 |
| SOL | 1698 | 48.1 | 49.4 | $-1448.67 |
| XRP | 1753 | 48.6 | 49.2 | $-1028.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
