# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1621 windows, 39004 settled trades, 345 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 824 | 34.2 | 35.2 | $-651.33 | -7.9% | $348.67 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3846 | 50.9 | 50.0 | $-1004.52 | -2.6% | $-4.52 | -1.6 | done | can't tell from luck |
| value_ev10 | 1952 | 38.3 | 39.0 | $-1134.66 | -5.8% | $-134.66 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3217 | 51.0 | 50.9 | $-1480.99 | -4.6% | $-480.99 | -2.7 | done | losing for real |
| value_ev5 | 2920 | 40.3 | 41.0 | $-1565.07 | -5.4% | $-565.07 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3217 | 49.0 | 49.2 | $-1741.56 | -5.4% | $-741.56 | -3.1 | done | losing for real |
| trend_filter | 2286 | 48.5 | 50.4 | $-2048.85 | -9.0% | $-1048.85 | -4.4 | done | losing for real |
| coinflip | 5632 | 50.1 | 49.9 | $-2318.91 | -4.1% | $-1318.91 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3846 | 49.1 | 50.2 | $-2375.60 | -6.2% | $-1375.60 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5632 | 50.2 | 51.3 | $-3491.91 | -6.2% | $-2491.91 | -4.8 | done | losing for real |
| always_up | 5632 | 48.1 | 49.1 | $-3675.75 | -6.5% | $-2675.75 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10415 | 47.9 | 48.6 | $-5942.99 |
| ETH | 11279 | 47.9 | 47.7 | $-5961.92 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
