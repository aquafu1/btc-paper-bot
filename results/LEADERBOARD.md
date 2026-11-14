# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 330 windows, 8802 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 703 | 53.3 | 51.7 | $-73.09 | -1.0% | $926.91 | -0.3 | done | can't tell from luck |
| value_ev20 | 175 | 36.0 | 36.6 | $-103.62 | -5.9% | $896.38 | -0.6 | Sat 6:45 PM | too few trades (175/200) |
| reversal_15m_0.10pct | 871 | 52.9 | 52.0 | $-216.81 | -2.5% | $783.19 | -0.8 | done | can't tell from luck |
| value_ev10 | 428 | 38.6 | 40.3 | $-346.99 | -8.1% | $653.01 | -1.4 | done | can't tell from luck |
| value_ev5 | 635 | 40.2 | 42.0 | $-532.77 | -8.4% | $467.23 | -1.8 | done | can't tell from luck |
| trend_filter | 480 | 44.8 | 50.3 | $-743.78 | -15.5% | $256.22 | -3.5 | done | losing for real |
| coinflip | 1312 | 50.0 | 50.9 | $-759.72 | -5.8% | $240.28 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 703 | 46.7 | 49.9 | $-792.38 | -11.3% | $207.62 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 871 | 47.1 | 49.8 | $-837.30 | -9.6% | $162.70 | -2.9 | done | losing for real |
| always_up | 1312 | 47.9 | 50.3 | $-1166.97 | -8.9% | $-166.97 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1312 | 48.3 | 51.2 | $-1259.17 | -9.6% | $-259.17 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1965 | 46.6 | 49.3 | $-1830.71 |
| ETH | 2207 | 47.1 | 48.7 | $-1914.59 |
| SOL | 2295 | 47.8 | 49.2 | $-1863.95 |
| XRP | 2335 | 48.7 | 49.0 | $-1223.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
