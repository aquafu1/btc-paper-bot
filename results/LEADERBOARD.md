# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 898 windows, 24772 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1137 | 38.3 | 39.1 | $-604.14 | -5.3% | $395.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2093 | 49.9 | 49.8 | $-961.40 | -4.6% | $38.60 | -2.1 | done | losing for real |
| value_ev5 | 1718 | 39.9 | 41.0 | $-997.05 | -5.8% | $2.95 | -2.0 | done | losing for real |
| trend_filter | 1465 | 50.0 | 51.0 | $-1014.54 | -6.9% | $-14.54 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2525 | 50.5 | 50.4 | $-1021.35 | -4.0% | $-21.35 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2093 | 50.1 | 50.9 | $-1357.05 | -6.5% | $-357.05 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2525 | 49.5 | 50.4 | $-1373.90 | -5.4% | $-373.90 | -2.8 | done | losing for real |
| coinflip | 3584 | 50.3 | 50.3 | $-1555.07 | -4.3% | $-555.07 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3584 | 51.3 | 51.7 | $-1641.43 | -4.6% | $-641.43 | -2.8 | done | losing for real |
| always_up | 3584 | 46.9 | 49.6 | $-3520.70 | -9.8% | $-2520.70 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5643 | 48.3 | 49.1 | $-3004.34 |
| ETH | 6161 | 48.2 | 48.5 | $-3755.02 |
| SOL | 6469 | 48.2 | 48.6 | $-3665.17 |
| XRP | 6499 | 48.3 | 48.5 | $-3723.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
