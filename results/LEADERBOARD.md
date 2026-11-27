# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1593 windows, 38646 settled trades, 412 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 814 | 34.5 | 35.1 | $-575.00 | -7.1% | $425.00 | -1.5 | done | can't tell from luck |
| value_ev10 | 1922 | 38.5 | 39.0 | $-999.67 | -5.2% | $0.33 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3815 | 50.9 | 50.0 | $-1003.04 | -2.6% | $-3.04 | -1.6 | done | can't tell from luck |
| value_ev5 | 2885 | 40.5 | 41.0 | $-1440.38 | -5.0% | $-440.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3196 | 51.0 | 50.9 | $-1478.51 | -4.6% | $-478.51 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3196 | 49.0 | 49.2 | $-1715.71 | -5.4% | $-715.71 | -3.0 | done | losing for real |
| trend_filter | 2272 | 48.5 | 50.3 | $-2026.82 | -8.9% | $-1026.82 | -4.4 | done | losing for real |
| coinflip | 5577 | 50.1 | 49.9 | $-2278.56 | -4.1% | $-1278.56 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3815 | 49.1 | 50.2 | $-2353.88 | -6.2% | $-1353.88 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5577 | 50.1 | 51.3 | $-3508.92 | -6.3% | $-2508.92 | -4.8 | done | losing for real |
| always_up | 5577 | 48.2 | 49.1 | $-3547.75 | -6.4% | $-2547.75 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10263 | 48.0 | 48.6 | $-5760.19 |
| ETH | 11073 | 48.0 | 47.7 | $-5583.83 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
