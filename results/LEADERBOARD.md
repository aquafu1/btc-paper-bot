# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 137 windows, 3443 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 240 | 62.9 | 53.1 | $+383.39 | +16.0% | $1383.39 | +2.7 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 329 | 57.8 | 52.2 | $+271.39 | +8.2% | $1271.39 | +1.6 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 3:30 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 540 | 51.7 | 51.1 | $-170.39 | -3.2% | $829.61 | -0.8 | done | can't tell from luck |
| coinflip | 540 | 51.5 | 51.0 | $-203.58 | -3.8% | $796.42 | -0.9 | done | can't tell from luck |
| value_ev10 | 183 | 37.7 | 40.6 | $-215.28 | -11.8% | $784.72 | -1.4 | Thu 7:00 AM | too few trades (183/200) |
| value_ev5 | 261 | 38.3 | 42.1 | $-345.63 | -13.2% | $654.37 | -1.9 | done | can't tell from luck |
| trend_filter | 174 | 39.7 | 49.0 | $-381.43 | -21.9% | $618.57 | -2.9 | Thu 9:00 AM | too few trades (174/200) |
| momentum_15m_0.10pct | 329 | 42.2 | 50.0 | $-593.92 | -18.1% | $406.08 | -3.3 | done | losing for real |
| always_up | 540 | 46.7 | 50.1 | $-606.08 | -11.2% | $393.92 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 240 | 37.1 | 49.1 | $-637.49 | -26.6% | $362.51 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 739 | 45.5 | 49.6 | $-810.87 |
| ETH | 854 | 44.8 | 48.8 | $-1019.35 |
| SOL | 908 | 48.8 | 48.7 | $-555.47 |
| XRP | 942 | 50.4 | 49.0 | $-248.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
