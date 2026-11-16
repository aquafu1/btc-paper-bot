# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 534 windows, 14759 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1260 | 51.6 | 49.8 | $-102.51 | -0.8% | $897.49 | -0.3 | done | can't tell from luck |
| value_ev20 | 281 | 34.5 | 35.5 | $-222.64 | -7.9% | $777.36 | -1.0 | done | can't tell from luck |
| trend_filter | 863 | 50.2 | 50.8 | $-472.77 | -5.5% | $527.23 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1496 | 50.0 | 49.7 | $-553.53 | -3.7% | $446.47 | -1.4 | done | can't tell from luck |
| value_ev10 | 690 | 38.0 | 39.7 | $-580.63 | -8.4% | $419.37 | -1.8 | done | can't tell from luck |
| value_ev5 | 1029 | 40.1 | 41.5 | $-746.07 | -7.3% | $253.93 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1496 | 50.0 | 51.4 | $-1080.99 | -7.2% | $-80.99 | -2.9 | done | losing for real |
| coinflip | 2128 | 49.9 | 50.6 | $-1204.35 | -5.7% | $-204.35 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1260 | 48.4 | 51.3 | $-1284.75 | -10.2% | $-284.75 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2128 | 49.8 | 51.7 | $-1602.70 | -7.5% | $-602.70 | -3.6 | done | losing for real |
| always_up | 2128 | 46.6 | 50.1 | $-2409.88 | -11.3% | $-1409.88 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3347 | 47.5 | 49.3 | $-2685.01 |
| ETH | 3681 | 48.0 | 48.7 | $-2443.07 |
| SOL | 3848 | 47.7 | 48.9 | $-2858.76 |
| XRP | 3883 | 48.4 | 48.8 | $-2273.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
