# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 717 windows, 19766 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2024 | 51.6 | 50.8 | $-506.87 | -2.5% | $493.13 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1659 | 50.2 | 49.5 | $-542.73 | -3.3% | $457.27 | -1.3 | done | can't tell from luck |
| value_ev10 | 911 | 38.0 | 39.1 | $-602.57 | -6.6% | $397.43 | -1.6 | done | can't tell from luck |
| value_ev5 | 1372 | 40.7 | 41.1 | $-668.08 | -4.9% | $331.92 | -1.5 | done | can't tell from luck |
| trend_filter | 1158 | 50.2 | 50.9 | $-671.90 | -5.8% | $328.10 | -2.0 | done | losing for real |
| coinflip | 2860 | 50.2 | 50.3 | $-1211.28 | -4.2% | $-211.28 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1659 | 49.8 | 51.3 | $-1242.01 | -7.5% | $-242.01 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2024 | 48.4 | 50.0 | $-1441.39 | -7.1% | $-441.39 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2860 | 51.0 | 51.8 | $-1445.28 | -5.1% | $-445.28 | -2.8 | done | losing for real |
| always_up | 2860 | 47.3 | 49.5 | $-2459.48 | -8.6% | $-1459.48 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4477 | 48.1 | 49.1 | $-2737.33 |
| ETH | 4920 | 48.3 | 48.5 | $-2903.81 |
| SOL | 5157 | 48.1 | 48.7 | $-3040.88 |
| XRP | 5212 | 48.6 | 48.4 | $-2423.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
