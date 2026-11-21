# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1027 windows, 28595 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 530 | 34.7 | 35.1 | $-278.51 | -5.3% | $721.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2912 | 51.1 | 50.5 | $-868.97 | -3.0% | $131.03 | -1.6 | done | can't tell from luck |
| value_ev10 | 1315 | 37.6 | 39.2 | $-954.55 | -7.3% | $45.45 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2459 | 49.9 | 49.6 | $-1062.65 | -4.3% | $-62.65 | -2.1 | done | losing for real |
| trend_filter | 1714 | 49.5 | 50.7 | $-1271.06 | -7.4% | $-271.06 | -3.2 | done | losing for real |
| value_ev5 | 1991 | 39.5 | 41.0 | $-1383.37 | -6.9% | $-383.37 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2459 | 50.1 | 51.0 | $-1647.90 | -6.7% | $-647.90 | -3.4 | done | losing for real |
| coinflip | 4101 | 50.4 | 50.4 | $-1726.73 | -4.2% | $-726.73 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2912 | 48.9 | 50.3 | $-1953.42 | -6.7% | $-953.42 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4101 | 50.6 | 51.5 | $-2295.23 | -5.6% | $-1295.23 | -3.7 | done | losing for real |
| always_up | 4101 | 47.4 | 49.5 | $-3563.41 | -8.7% | $-2563.41 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6522 | 48.3 | 49.1 | $-3556.46 |
| ETH | 7098 | 48.1 | 48.5 | $-4401.56 |
| SOL | 7466 | 48.2 | 48.6 | $-4275.45 |
| XRP | 7509 | 48.1 | 48.4 | $-4772.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
