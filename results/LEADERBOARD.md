# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 954 windows, 26449 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1201 | 38.1 | 39.1 | $-678.29 | -5.6% | $321.71 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2705 | 51.2 | 50.6 | $-791.71 | -2.9% | $208.29 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2261 | 50.2 | 49.7 | $-855.64 | -3.8% | $144.36 | -1.8 | done | can't tell from luck |
| trend_filter | 1582 | 50.1 | 50.8 | $-1004.56 | -6.3% | $-4.56 | -2.6 | done | losing for real |
| value_ev5 | 1823 | 39.8 | 41.0 | $-1070.24 | -5.9% | $-70.24 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2261 | 49.8 | 51.0 | $-1650.18 | -7.3% | $-650.18 | -3.6 | done | losing for real |
| coinflip | 3808 | 50.2 | 50.4 | $-1711.59 | -4.5% | $-711.59 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2705 | 48.8 | 50.2 | $-1863.81 | -6.9% | $-863.81 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3808 | 50.9 | 51.5 | $-1892.35 | -5.0% | $-892.35 | -3.2 | done | losing for real |
| always_up | 3808 | 46.8 | 49.6 | $-3814.75 | -10.0% | $-2814.75 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6029 | 48.1 | 49.0 | $-3479.98 |
| ETH | 6572 | 48.1 | 48.5 | $-4047.49 |
| SOL | 6898 | 48.3 | 48.6 | $-3826.79 |
| XRP | 6950 | 48.2 | 48.5 | $-4133.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
