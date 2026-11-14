# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 290 windows, 7671 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 756 | 54.1 | 51.8 | $-2.62 | -0.0% | $997.38 | -0.0 | done | can't tell from luck |
| value_ev20 | 143 | 36.4 | 36.4 | $-84.69 | -5.9% | $915.31 | -0.6 | Sun 3:00 AM | too few trades (143/200) |
| reversal_60m_0.30pct | 615 | 52.2 | 51.8 | $-220.58 | -3.6% | $779.42 | -0.9 | done | can't tell from luck |
| value_ev10 | 373 | 38.9 | 40.5 | $-303.14 | -8.1% | $696.86 | -1.3 | done | can't tell from luck |
| trend_filter | 409 | 46.9 | 50.3 | $-453.61 | -11.1% | $546.39 | -2.3 | done | losing for real |
| value_ev5 | 548 | 40.3 | 42.1 | $-471.67 | -8.6% | $528.33 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 615 | 47.8 | 49.8 | $-542.32 | -8.8% | $457.68 | -2.2 | done | losing for real |
| coinflip | 1152 | 50.2 | 50.9 | $-639.85 | -5.6% | $360.15 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1152 | 49.5 | 51.4 | $-892.39 | -7.7% | $107.61 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 756 | 45.9 | 49.8 | $-897.03 | -11.9% | $102.97 | -3.3 | done | losing for real |
| always_up | 1152 | 47.4 | 50.2 | $-1126.10 | -9.8% | $-126.10 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1709 | 47.0 | 49.4 | $-1474.17 |
| ETH | 1914 | 47.3 | 48.7 | $-1635.56 |
| SOL | 1996 | 48.3 | 49.3 | $-1515.54 |
| XRP | 2052 | 48.8 | 49.0 | $-1008.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
