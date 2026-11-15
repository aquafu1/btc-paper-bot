# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 416 windows, 11452 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| value_ev10 | 535 | 39.8 | 40.4 | $-271.49 | -5.1% | $728.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 982 | 50.7 | 50.1 | $-287.89 | -2.9% | $712.11 | -0.9 | done | can't tell from luck |
| value_ev5 | 804 | 41.8 | 42.1 | $-370.32 | -4.6% | $629.68 | -1.1 | done | can't tell from luck |
| trend_filter | 658 | 49.8 | 50.8 | $-382.59 | -5.8% | $617.41 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1154 | 49.5 | 49.9 | $-525.67 | -4.6% | $474.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1154 | 50.5 | 51.8 | $-770.90 | -6.7% | $229.10 | -2.4 | done | losing for real |
| coinflip | 1658 | 50.3 | 50.9 | $-811.51 | -4.9% | $188.49 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 982 | 49.3 | 51.8 | $-872.14 | -8.9% | $127.86 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1658 | 49.7 | 51.6 | $-1181.90 | -7.1% | $-181.90 | -3.0 | done | losing for real |
| always_up | 1658 | 45.8 | 50.7 | $-2178.07 | -13.1% | $-1178.07 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2596 | 47.7 | 49.4 | $-1905.65 |
| ETH | 2877 | 47.9 | 49.0 | $-1819.09 |
| SOL | 2961 | 47.7 | 49.5 | $-2439.28 |
| XRP | 3018 | 48.8 | 49.3 | $-1645.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
