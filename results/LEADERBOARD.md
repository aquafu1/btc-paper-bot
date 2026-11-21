# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 952 windows, 26389 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 486 | 35.2 | 34.9 | $-144.35 | -3.0% | $855.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1198 | 38.1 | 39.1 | $-648.29 | -5.4% | $351.71 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2700 | 51.3 | 50.6 | $-774.00 | -2.9% | $226.00 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2255 | 50.1 | 49.7 | $-883.20 | -3.9% | $116.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1819 | 39.9 | 41.0 | $-1030.24 | -5.7% | $-30.24 | -2.0 | done | losing for real |
| trend_filter | 1576 | 49.9 | 50.8 | $-1048.86 | -6.7% | $-48.86 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2255 | 49.9 | 51.0 | $-1607.20 | -7.1% | $-607.20 | -3.5 | done | losing for real |
| coinflip | 3800 | 50.2 | 50.4 | $-1721.52 | -4.5% | $-721.52 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2700 | 48.7 | 50.2 | $-1868.21 | -6.9% | $-868.21 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3800 | 50.8 | 51.5 | $-1951.58 | -5.1% | $-951.58 | -3.3 | done | losing for real |
| always_up | 3800 | 46.8 | 49.6 | $-3769.69 | -9.9% | $-2769.69 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6016 | 48.1 | 49.0 | $-3471.47 |
| ETH | 6562 | 48.1 | 48.5 | $-4051.46 |
| SOL | 6879 | 48.2 | 48.6 | $-3815.90 |
| XRP | 6932 | 48.2 | 48.5 | $-4108.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
