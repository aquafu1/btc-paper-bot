# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1308 windows, 34801 settled trades, 404 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 686 | 34.3 | 35.3 | $-520.82 | -7.6% | $479.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1677 | 38.8 | 39.2 | $-787.85 | -4.7% | $212.15 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3490 | 50.9 | 50.2 | $-1025.80 | -2.9% | $-25.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 2532 | 40.4 | 41.1 | $-1284.55 | -5.1% | $-284.55 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2921 | 49.4 | 49.4 | $-1364.71 | -4.7% | $-364.71 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2921 | 50.6 | 51.0 | $-1599.78 | -5.5% | $-599.78 | -3.0 | done | losing for real |
| trend_filter | 2066 | 48.8 | 50.5 | $-1711.78 | -8.3% | $-711.78 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3490 | 49.1 | 50.2 | $-2192.99 | -6.3% | $-1192.99 | -3.8 | done | losing for real |
| coinflip | 5006 | 50.0 | 50.1 | $-2248.78 | -4.5% | $-1248.78 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5006 | 50.4 | 51.4 | $-2898.31 | -5.8% | $-1898.31 | -4.2 | done | losing for real |
| always_up | 5006 | 47.9 | 49.3 | $-3633.67 | -7.3% | $-2633.67 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8418 | 48.0 | 48.8 | $-4902.70 |
| ETH | 9073 | 48.2 | 48.2 | $-4782.08 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
