# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1003 windows, 27890 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 515 | 34.2 | 34.9 | $-306.26 | -5.9% | $693.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2841 | 51.0 | 50.4 | $-896.88 | -3.2% | $103.12 | -1.7 | done | can't tell from luck |
| value_ev10 | 1277 | 37.4 | 39.1 | $-929.88 | -7.3% | $70.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2397 | 50.0 | 49.7 | $-1026.76 | -4.3% | $-26.76 | -2.1 | done | losing for real |
| trend_filter | 1671 | 49.7 | 50.8 | $-1200.99 | -7.2% | $-200.99 | -3.0 | done | losing for real |
| value_ev5 | 1936 | 39.5 | 41.0 | $-1298.44 | -6.7% | $-298.44 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2397 | 50.0 | 50.9 | $-1645.64 | -6.9% | $-645.64 | -3.4 | done | losing for real |
| coinflip | 4005 | 50.4 | 50.4 | $-1711.17 | -4.3% | $-711.17 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2841 | 49.0 | 50.3 | $-1907.20 | -6.7% | $-907.20 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4005 | 50.7 | 51.5 | $-2207.53 | -5.5% | $-1207.53 | -3.6 | done | losing for real |
| always_up | 4005 | 47.1 | 49.6 | $-3778.65 | -9.4% | $-2778.65 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6363 | 48.2 | 49.0 | $-3603.32 |
| ETH | 6923 | 48.0 | 48.5 | $-4494.45 |
| SOL | 7292 | 48.2 | 48.6 | $-4115.08 |
| XRP | 7312 | 48.1 | 48.4 | $-4696.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
