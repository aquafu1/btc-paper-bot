# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1596 windows, 38705 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 816 | 34.4 | 35.1 | $-595.00 | -7.3% | $405.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3819 | 50.9 | 50.0 | $-989.23 | -2.6% | $10.77 | -1.6 | done | can't tell from luck |
| value_ev10 | 1928 | 38.5 | 39.0 | $-1005.86 | -5.2% | $-5.86 | -1.9 | done | can't tell from luck |
| value_ev5 | 2891 | 40.5 | 41.0 | $-1446.57 | -5.0% | $-446.57 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3202 | 51.1 | 50.9 | $-1464.05 | -4.6% | $-464.05 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3202 | 48.9 | 49.2 | $-1739.43 | -5.4% | $-739.43 | -3.1 | done | losing for real |
| trend_filter | 2276 | 48.5 | 50.4 | $-2030.54 | -8.9% | $-1030.54 | -4.4 | done | losing for real |
| coinflip | 5584 | 50.0 | 49.9 | $-2348.56 | -4.2% | $-1348.56 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3819 | 49.1 | 50.2 | $-2361.64 | -6.2% | $-1361.64 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5584 | 50.1 | 51.3 | $-3485.95 | -6.2% | $-2485.95 | -4.8 | done | losing for real |
| always_up | 5584 | 48.2 | 49.1 | $-3581.47 | -6.4% | $-2581.47 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10286 | 48.0 | 48.6 | $-5766.38 |
| ETH | 11109 | 48.0 | 47.7 | $-5697.69 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
