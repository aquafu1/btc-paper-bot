# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1647 windows, 39321 settled trades, 400 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 836 | 34.4 | 35.2 | $-603.68 | -7.2% | $396.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3867 | 50.8 | 49.9 | $-1027.22 | -2.7% | $-27.22 | -1.6 | done | can't tell from luck |
| value_ev10 | 1975 | 38.4 | 39.0 | $-1092.71 | -5.5% | $-92.71 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3235 | 51.1 | 50.9 | $-1452.53 | -4.5% | $-452.53 | -2.6 | done | losing for real |
| value_ev5 | 2952 | 40.4 | 41.0 | $-1555.41 | -5.3% | $-555.41 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3235 | 48.9 | 49.3 | $-1780.63 | -5.5% | $-780.63 | -3.1 | done | losing for real |
| trend_filter | 2302 | 48.4 | 50.4 | $-2068.35 | -9.0% | $-1068.35 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3867 | 49.2 | 50.2 | $-2352.58 | -6.1% | $-1352.58 | -3.8 | done | losing for real |
| coinflip | 5684 | 49.9 | 49.9 | $-2504.08 | -4.4% | $-1504.08 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5684 | 50.2 | 51.3 | $-3497.06 | -6.2% | $-2497.06 | -4.8 | done | losing for real |
| always_up | 5684 | 48.2 | 49.0 | $-3549.52 | -6.2% | $-2549.52 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10566 | 47.9 | 48.6 | $-5931.52 |
| ETH | 11445 | 47.9 | 47.6 | $-5968.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
