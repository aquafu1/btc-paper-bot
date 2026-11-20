# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 899 windows, 24795 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1137 | 38.3 | 39.1 | $-604.14 | -5.3% | $395.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2094 | 49.9 | 49.8 | $-971.40 | -4.6% | $28.60 | -2.1 | done | losing for real |
| value_ev5 | 1719 | 40.0 | 41.0 | $-984.75 | -5.7% | $15.25 | -2.0 | done | losing for real |
| trend_filter | 1467 | 50.0 | 51.0 | $-1012.23 | -6.9% | $-12.23 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2528 | 50.4 | 50.4 | $-1051.35 | -4.2% | $-51.35 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2528 | 49.6 | 50.4 | $-1339.20 | -5.3% | $-339.20 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2094 | 50.1 | 50.8 | $-1346.56 | -6.4% | $-346.56 | -3.0 | done | losing for real |
| coinflip | 3588 | 50.3 | 50.3 | $-1552.26 | -4.3% | $-552.26 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3588 | 51.3 | 51.7 | $-1616.72 | -4.5% | $-616.72 | -2.8 | done | losing for real |
| always_up | 3588 | 46.9 | 49.6 | $-3475.50 | -9.7% | $-2475.50 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5648 | 48.3 | 49.1 | $-2994.11 |
| ETH | 6166 | 48.3 | 48.5 | $-3715.71 |
| SOL | 6475 | 48.2 | 48.6 | $-3663.71 |
| XRP | 6506 | 48.3 | 48.5 | $-3681.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
