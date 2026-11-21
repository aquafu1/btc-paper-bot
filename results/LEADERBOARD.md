# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 964 windows, 26688 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 493 | 34.9 | 34.8 | $-189.50 | -3.8% | $810.50 | -0.6 | done | can't tell from luck |
| value_ev10 | 1218 | 38.1 | 39.1 | $-679.76 | -5.6% | $320.24 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2725 | 51.3 | 50.5 | $-699.02 | -2.6% | $300.98 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2272 | 50.0 | 49.7 | $-921.20 | -4.1% | $78.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1846 | 39.9 | 41.0 | $-1040.59 | -5.6% | $-40.59 | -2.0 | done | losing for real |
| trend_filter | 1593 | 49.9 | 50.9 | $-1063.19 | -6.7% | $-63.19 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2272 | 50.0 | 51.0 | $-1561.30 | -6.9% | $-561.30 | -3.3 | done | losing for real |
| coinflip | 3848 | 50.2 | 50.4 | $-1781.27 | -4.6% | $-781.27 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2725 | 48.7 | 50.3 | $-1948.41 | -7.2% | $-948.41 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3848 | 50.9 | 51.6 | $-1956.16 | -5.1% | $-956.16 | -3.3 | done | losing for real |
| always_up | 3848 | 46.9 | 49.6 | $-3751.44 | -9.7% | $-2751.44 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6079 | 48.1 | 49.0 | $-3506.92 |
| ETH | 6630 | 48.1 | 48.5 | $-4119.87 |
| SOL | 6972 | 48.3 | 48.6 | $-3748.76 |
| XRP | 7007 | 48.2 | 48.5 | $-4216.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
