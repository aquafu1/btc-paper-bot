# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 953 windows, 26441 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1201 | 38.1 | 39.1 | $-678.29 | -5.6% | $321.71 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2704 | 51.3 | 50.6 | $-781.71 | -2.9% | $218.29 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2260 | 50.2 | 49.7 | $-864.22 | -3.8% | $135.78 | -1.8 | done | can't tell from luck |
| trend_filter | 1581 | 50.0 | 50.8 | $-1013.14 | -6.4% | $-13.14 | -2.6 | done | losing for real |
| value_ev5 | 1823 | 39.8 | 41.0 | $-1070.24 | -5.9% | $-70.24 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2260 | 49.8 | 51.0 | $-1640.18 | -7.3% | $-640.18 | -3.5 | done | losing for real |
| coinflip | 3807 | 50.2 | 50.4 | $-1720.17 | -4.5% | $-720.17 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2704 | 48.7 | 50.2 | $-1872.39 | -6.9% | $-872.39 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3807 | 50.9 | 51.5 | $-1900.93 | -5.0% | $-900.93 | -3.2 | done | losing for real |
| always_up | 3807 | 46.8 | 49.6 | $-3804.75 | -10.0% | $-2804.75 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6029 | 48.1 | 49.0 | $-3479.98 |
| ETH | 6572 | 48.1 | 48.5 | $-4047.49 |
| SOL | 6898 | 48.3 | 48.6 | $-3826.79 |
| XRP | 6942 | 48.2 | 48.5 | $-4146.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
