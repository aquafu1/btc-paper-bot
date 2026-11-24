# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1274 windows, 34258 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 671 | 34.1 | 35.3 | $-520.36 | -7.8% | $479.64 | -1.5 | done | can't tell from luck |
| value_ev10 | 1645 | 38.6 | 39.2 | $-833.77 | -5.1% | $166.23 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3433 | 50.6 | 50.2 | $-1212.27 | -3.5% | $-212.27 | -2.1 | done | losing for real |
| value_ev5 | 2486 | 40.4 | 41.1 | $-1286.74 | -5.2% | $-286.74 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2872 | 49.5 | 49.4 | $-1318.28 | -4.6% | $-318.28 | -2.5 | done | losing for real |
| trend_filter | 2029 | 49.0 | 50.4 | $-1608.58 | -7.9% | $-608.58 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2872 | 50.5 | 51.0 | $-1660.57 | -5.8% | $-660.57 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3433 | 49.4 | 50.2 | $-2011.81 | -5.9% | $-1011.81 | -3.5 | done | losing for real |
| coinflip | 4939 | 49.9 | 50.1 | $-2279.22 | -4.6% | $-1279.22 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4939 | 50.5 | 51.4 | $-2774.06 | -5.6% | $-1774.06 | -4.1 | done | losing for real |
| always_up | 4939 | 47.8 | 49.4 | $-3641.04 | -7.4% | $-2641.04 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8149 | 48.0 | 48.9 | $-4815.21 |
| ETH | 8799 | 48.2 | 48.3 | $-4747.25 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
