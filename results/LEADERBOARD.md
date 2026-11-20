# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 925 windows, 25572 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2177 | 50.2 | 49.8 | $-861.19 | -4.0% | $138.81 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2608 | 50.6 | 50.5 | $-1030.66 | -4.0% | $-30.66 | -2.0 | done | losing for real |
| trend_filter | 1520 | 50.0 | 51.0 | $-1033.57 | -6.8% | $-33.57 | -2.7 | done | losing for real |
| value_ev5 | 1761 | 39.8 | 41.0 | $-1047.50 | -5.9% | $-47.50 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2608 | 49.4 | 50.3 | $-1457.33 | -5.6% | $-457.33 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2177 | 49.8 | 50.9 | $-1544.48 | -7.1% | $-544.48 | -3.4 | done | losing for real |
| coinflip | 3695 | 50.3 | 50.3 | $-1591.59 | -4.3% | $-591.59 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3695 | 51.0 | 51.6 | $-1875.45 | -5.1% | $-875.45 | -3.2 | done | losing for real |
| always_up | 3695 | 46.8 | 49.7 | $-3762.13 | -10.2% | $-2762.13 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5826 | 48.2 | 49.1 | $-3340.04 |
| ETH | 6363 | 48.2 | 48.5 | $-3981.61 |
| SOL | 6666 | 48.2 | 48.6 | $-3876.84 |
| XRP | 6717 | 48.3 | 48.5 | $-3784.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
