# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 765 windows, 21096 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2158 | 51.4 | 50.6 | $-541.01 | -2.5% | $458.99 | -1.2 | done | can't tell from luck |
| value_ev10 | 963 | 38.0 | 39.1 | $-611.05 | -6.3% | $388.95 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1782 | 49.9 | 49.6 | $-688.46 | -3.9% | $311.54 | -1.6 | done | can't tell from luck |
| trend_filter | 1240 | 49.9 | 50.9 | $-785.43 | -6.3% | $214.57 | -2.3 | done | losing for real |
| value_ev5 | 1456 | 40.2 | 41.1 | $-817.45 | -5.6% | $182.55 | -1.8 | done | can't tell from luck |
| coinflip | 3054 | 50.4 | 50.3 | $-1155.76 | -3.8% | $-155.76 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1782 | 50.1 | 51.2 | $-1235.67 | -6.9% | $-235.67 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3054 | 51.0 | 51.7 | $-1533.37 | -5.0% | $-533.37 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2158 | 48.6 | 50.2 | $-1550.39 | -7.2% | $-550.39 | -3.4 | done | losing for real |
| always_up | 3054 | 47.1 | 49.6 | $-2831.75 | -9.3% | $-1831.75 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4788 | 48.2 | 49.1 | $-2875.70 |
| ETH | 5262 | 48.1 | 48.6 | $-3394.00 |
| SOL | 5493 | 48.1 | 48.6 | $-3217.18 |
| XRP | 5553 | 48.6 | 48.5 | $-2564.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
