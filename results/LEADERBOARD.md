# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 929 windows, 25680 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2191 | 50.1 | 49.8 | $-933.26 | -4.3% | $66.74 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2621 | 50.8 | 50.5 | $-933.73 | -3.6% | $66.27 | -1.8 | done | can't tell from luck |
| value_ev5 | 1763 | 39.8 | 41.0 | $-1047.33 | -5.9% | $-47.33 | -2.1 | done | losing for real |
| trend_filter | 1527 | 49.9 | 51.0 | $-1065.88 | -7.0% | $-65.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2191 | 49.9 | 50.9 | $-1505.41 | -6.9% | $-505.41 | -3.3 | done | losing for real |
| coinflip | 3710 | 50.4 | 50.4 | $-1533.95 | -4.1% | $-533.95 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2621 | 49.2 | 50.3 | $-1587.33 | -6.1% | $-587.33 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3710 | 51.0 | 51.6 | $-1878.16 | -5.1% | $-878.16 | -3.2 | done | losing for real |
| always_up | 3710 | 46.8 | 49.7 | $-3770.84 | -10.2% | $-2770.84 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5851 | 48.2 | 49.1 | $-3380.73 |
| ETH | 6385 | 48.2 | 48.6 | $-3955.65 |
| SOL | 6697 | 48.2 | 48.6 | $-3892.57 |
| XRP | 6747 | 48.3 | 48.5 | $-3805.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
