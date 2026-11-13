# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 220 windows, 5746 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 568 | 56.2 | 52.7 | $+193.10 | +3.4% | $1193.10 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 451 | 55.2 | 52.5 | $+90.04 | +2.0% | $1090.04 | +0.4 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 8:45 AM | too few trades (105/200) |
| value_ev10 | 280 | 37.1 | 40.9 | $-368.28 | -13.2% | $631.72 | -1.9 | done | can't tell from luck |
| trend_filter | 299 | 44.5 | 50.1 | $-439.49 | -14.7% | $560.51 | -2.6 | done | losing for real |
| value_ev5 | 408 | 39.2 | 42.7 | $-490.08 | -12.0% | $509.92 | -2.2 | done | losing for real |
| coinflip | 872 | 50.1 | 51.0 | $-517.36 | -5.9% | $482.64 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 872 | 50.5 | 51.5 | $-520.36 | -6.0% | $479.64 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 451 | 44.8 | 49.7 | $-616.71 | -13.7% | $383.29 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 568 | 43.8 | 49.7 | $-862.43 | -15.2% | $137.57 | -3.7 | done | losing for real |
| always_up | 872 | 46.6 | 50.3 | $-1002.66 | -11.5% | $-2.66 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1285 | 46.2 | 49.7 | $-1343.41 |
| ETH | 1431 | 46.5 | 49.0 | $-1405.11 |
| SOL | 1483 | 48.0 | 49.4 | $-1209.83 |
| XRP | 1547 | 49.4 | 49.4 | $-701.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
